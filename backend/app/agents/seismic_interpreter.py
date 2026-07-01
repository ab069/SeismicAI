import math


def analyze_horizon(amplitude: float, continuity: int, depth_m: float) -> dict:
    quality = "low"
    if amplitude > 0.7 and continuity > 70:
        quality = "high"
    elif amplitude > 0.4 and continuity > 40:
        quality = "medium"

    bright_spot = amplitude > 0.8 and continuity > 60
    dim_spot = amplitude < 0.2 and continuity < 30

    return {
        "horizon_quality": quality,
        "bright_spot": bright_spot,
        "dim_spot": dim_spot,
        "confidence_score": round((amplitude * 0.5 + continuity / 100 * 0.5) * 100, 1),
        "recommendation": "Further AVO analysis recommended" if bright_spot else "Routine interpretation"
    }


def calculate_prospect_risk(volume_oil_mmboe: float, volume_gas_bcf: float, probability: float, horizon_quality: str) -> dict:
    base_risk = 1 - probability
    quality_factor = {"high": 0.7, "medium": 1.0, "low": 1.3}.get(horizon_quality, 1.0)
    adjusted_risk = min(base_risk * quality_factor, 1.0)

    if adjusted_risk < 0.3:
        risk_level = "low"
    elif adjusted_risk < 0.6:
        risk_level = "medium"
    else:
        risk_level = "high"

    total_boe = volume_oil_mmboe + volume_gas_bcf / 6
    risk_adjusted_value = total_boe * probability * (1 - adjusted_risk)

    return {
        "risk_level": risk_level,
        "risk_score": round(adjusted_risk, 2),
        "total_boe_mmboe": round(total_boe, 2),
        "risk_adjusted_value_mmboe": round(risk_adjusted_value, 2),
        "recommendation": "Drill ready" if risk_level == "low" and total_boe > 10 else "Further evaluation needed"
    }


def estimate_resources(horizon_area_km2: float, amplitude: float, depth_m: float) -> dict:
    thickness_factor = max(0.1, amplitude * 10)
    porosity = min(0.3, max(0.05, (100 - depth_m / 100) / 100))
    saturation = min(0.8, max(0.2, amplitude * 0.6 + 0.2))

    volume_rock = horizon_area_km2 * 1_000_000 * thickness_factor
    pore_volume = volume_rock * porosity
    hydrocarbon_volume = pore_volume * saturation

    oil_mmboe = hydrocarbon_volume * 0.00629 * 0.5
    gas_bcf = hydrocarbon_volume * 0.00629 * 0.5 * 6

    return {
        "oil_mmboe": round(oil_mmboe, 2),
        "gas_bcf": round(gas_bcf, 2),
        "porosity": round(porosity, 3),
        "saturation": round(saturation, 3),
        "net_pay_m": round(thickness_factor, 1)
    }


def generate_interpretation_report(survey_name: str, findings: list[dict]) -> str:
    lines = [f"Seismic Interpretation Report", f"=" * 40, f"Survey: {survey_name}", f""]
    for f in findings:
        lines.append(f"- {f.get('horizon_name', 'Unknown')}: {f.get('horizon_quality', 'N/A')} quality, "
                     f"confidence {f.get('confidence_score', 0)}%")
        if f.get("bright_spot"):
            lines.append("  >> Bright spot anomaly detected")
    lines.append(f"")
    lines.append("Interpretation complete.")
    return "\n".join(lines)
