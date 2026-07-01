import { useState } from 'react'
import { useSeismicStore } from '../store/seismicStore'

const confidenceColors: Record<string, string> = {
  high: '#22c55e',
  medium: '#eab308',
  low: '#ef4444',
}

export default function SurveyList() {
  const surveys = useSeismicStore((s) => s.surveys)
  const [expanded, setExpanded] = useState<string | null>(null)

  return (
    <div style={{ marginBottom: 24 }}>
      <h3 style={{ color: '#7c3aed', marginBottom: 12 }}>Surveys</h3>
      {surveys.map((s) => (
        <div
          key={s.id}
          style={{
            background: '#1a1a2e',
            border: '1px solid #7c3aed44',
            borderRadius: 10,
            marginBottom: 8,
            padding: 12,
            cursor: 'pointer',
          }}
          onClick={() => setExpanded(expanded === s.id ? null : s.id)}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <strong>{s.survey_name}</strong>
            <span style={{
              background: '#7c3aed22',
              color: '#7c3aed',
              padding: '2px 10px',
              borderRadius: 12,
              fontSize: 12,
            }}>
              {s.survey_type}
            </span>
          </div>
          <div style={{ fontSize: 12, color: '#999', marginTop: 4 }}>{s.location} · {s.area_km2} km² · {s.status}</div>

          {expanded === s.id && (
            <div style={{ marginTop: 12, borderTop: '1px solid #333', paddingTop: 12 }}>
              <p style={{ margin: '2px 0', fontSize: 13 }}>Line: {s.line_km} km · Fold: {s.fold} · Resolution: {s.resolution_m}m</p>
              <p style={{ margin: '2px 0', fontSize: 13, color: '#7c3aed' }}>Horizons (demo) · Confidence: <span style={{ color: confidenceColors.medium }}>medium</span></p>
              <p style={{ margin: '2px 0', fontSize: 13, color: '#7c3aed' }}>Prospects (demo) · Risk: <span style={{ color: '#eab308' }}>medium</span></p>
            </div>
          )}
        </div>
      ))}
    </div>
  )
}
