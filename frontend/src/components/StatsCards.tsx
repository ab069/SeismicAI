interface StatsCardsProps {
  stats: {
    total_surveys: number
    total_area_km2: number
    total_prospects: number
    avg_probability: number
  } | null
}

export default function StatsCards({ stats }: StatsCardsProps) {
  if (!stats) return null

  const cards = [
    { label: 'Total Surveys', value: stats.total_surveys },
    { label: 'Total Area (km²)', value: stats.total_area_km2.toFixed(1) },
    { label: 'Prospects Identified', value: stats.total_prospects },
    { label: 'Avg Confidence', value: (stats.avg_probability * 100).toFixed(0) + '%' },
  ]

  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
        gap: 16,
        marginBottom: 24,
      }}
    >
      {cards.map((c) => (
        <div
          key={c.label}
          style={{
            background: '#1a1a2e',
            border: '1px solid #7c3aed44',
            borderRadius: 12,
            padding: '20px 16px',
            textAlign: 'center',
          }}
        >
          <div style={{ fontSize: 28, fontWeight: 700, color: '#7c3aed' }}>{c.value}</div>
          <div style={{ fontSize: 13, marginTop: 4, color: '#aaa' }}>{c.label}</div>
        </div>
      ))}
    </div>
  )
}
