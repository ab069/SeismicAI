import { useSeismicStore } from '../store/seismicStore'

const riskColors: Record<string, string> = {
  low: '#22c55e',
  medium: '#eab308',
  high: '#ef4444',
}

export default function ProspectList() {
  const prospects = useSeismicStore((s) => s.prospects)

  return (
    <div>
      <h3 style={{ color: '#7c3aed', marginBottom: 12 }}>Prospects</h3>
      {prospects.map((p) => (
        <div
          key={p.id}
          style={{
            background: '#1a1a2e',
            border: '1px solid #7c3aed44',
            borderRadius: 10,
            marginBottom: 8,
            padding: 12,
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <strong>{p.prospect_name}</strong>
            <span
              style={{
                background: `${riskColors[p.risk_level] || '#eab308'}22`,
                color: riskColors[p.risk_level] || '#eab308',
                padding: '2px 10px',
                borderRadius: 12,
                fontSize: 12,
                fontWeight: 600,
              }}
            >
              {p.risk_level}
            </span>
          </div>
          <div style={{ fontSize: 12, color: '#999', marginTop: 4 }}>
            Oil: {p.volume_oil_mmboe} MMBOE · Gas: {p.volume_gas_bcf} BCF · P: {p.probability} · {p.status}
          </div>
        </div>
      ))}
    </div>
  )
}
