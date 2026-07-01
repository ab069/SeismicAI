import json
import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.agents.seismic_interpreter import analyze_horizon, calculate_prospect_risk, estimate_resources, generate_interpretation_report

router = APIRouter()


@router.websocket("/ws/interpret")
async def websocket_interpret(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)

            action = msg.get("action")

            if action == "analyze_horizon":
                result = analyze_horizon(msg.get("amplitude", 0), msg.get("continuity", 0), msg.get("depth_m", 0))
                await websocket.send_json({"event": "horizon_analysis", "data": result})

            elif action == "risk_assessment":
                result = calculate_prospect_risk(
                    msg.get("volume_oil_mmboe", 0), msg.get("volume_gas_bcf", 0),
                    msg.get("probability", 0), msg.get("horizon_quality", "medium")
                )
                await websocket.send_json({"event": "risk_assessment", "data": result})

            elif action == "estimate_resources":
                result = estimate_resources(msg.get("horizon_area_km2", 0), msg.get("amplitude", 0), msg.get("depth_m", 0))
                await websocket.send_json({"event": "resource_estimate", "data": result})

            elif action == "full_report":
                findings = msg.get("findings", [])
                report = generate_interpretation_report(msg.get("survey_name", "Unknown"), findings)
                for line in report.split("\n"):
                    await websocket.send_json({"event": "report_line", "data": line})
                    await asyncio.sleep(0.05)
                await websocket.send_json({"event": "report_complete", "data": "Interpretation report generated"})

            else:
                await websocket.send_json({"event": "error", "data": f"Unknown action: {action}"})

    except WebSocketDisconnect:
        pass
