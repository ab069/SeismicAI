import { useWsStore } from '../store/wsStore'

export default function InterpretationFeed() {
  const connected = useWsStore((s) => s.connected)
  const events = useWsStore((s) => s.events)

  return (
    <div
      style={{
        background: '#1a1a2e',
        border: '1px solid #7c3aed44',
        borderRadius: 12,
        padding: 16,
        marginBottom: 24,
        maxHeight: 300,
        overflowY: 'auto',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 12 }}>
        <h3 style={{ margin: 0, color: '#7c3aed' }}>Real-Time Feed</h3>
        <span
          style={{
            width: 10,
            height: 10,
            borderRadius: '50%',
            background: connected ? '#22c55e' : '#ef4444',
            display: 'inline-block',
            marginTop: 6,
          }}
        />
      </div>
      {events.length === 0 && <p style={{ color: '#666', fontSize: 13 }}>No events yet. Create surveys to see interpretation activity.</p>}
      {events
        .slice()
        .reverse()
        .map((e, i) => (
          <div key={i} style={{ fontSize: 12, marginBottom: 4, borderBottom: '1px solid #222', paddingBottom: 4 }}>
            <span style={{ color: '#7c3aed' }}>[{e.event}]</span>{' '}
            <span style={{ color: '#ccc' }}>{typeof e.data === 'string' ? e.data : JSON.stringify(e.data).slice(0, 120)}</span>
          </div>
        ))}
    </div>
  )
}
