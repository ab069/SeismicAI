import { useState } from 'react'
import { useSeismicStore } from '../store/seismicStore'

export default function SurveyForm() {
  const [form, setForm] = useState({
    survey_name: '',
    location: '',
    survey_type: '3D',
    area_km2: 0,
    line_km: 0,
    fold: 0,
    resolution_m: 0,
  })
  const [msg, setMsg] = useState('')
  const fetchSurveys = useSeismicStore((s) => s.fetchSurveys)
  const fetchStats = useSeismicStore((s) => s.fetchStats)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await useSeismicStore.getState().submitSurvey(form)
      setMsg('Survey created')
      setForm({ survey_name: '', location: '', survey_type: '3D', area_km2: 0, line_km: 0, fold: 0, resolution_m: 0 })
      fetchSurveys()
      fetchStats()
    } catch {
      setMsg('Error creating survey')
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        background: '#1a1a2e',
        border: '1px solid #7c3aed44',
        borderRadius: 12,
        padding: 20,
        marginBottom: 24,
      }}
    >
      <h3 style={{ margin: '0 0 16px', color: '#7c3aed' }}>New Survey</h3>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
        <input placeholder="Survey name" value={form.survey_name} onChange={(e) => setForm({ ...form, survey_name: e.target.value })} required style={inp} />
        <input placeholder="Location" value={form.location} onChange={(e) => setForm({ ...form, location: e.target.value })} required style={inp} />
        <select value={form.survey_type} onChange={(e) => setForm({ ...form, survey_type: e.target.value })} style={inp}>
          <option value="2D">2D</option>
          <option value="3D">3D</option>
          <option value="4D">4D</option>
        </select>
        <input type="number" step="0.1" placeholder="Area (km²)" value={form.area_km2 || ''} onChange={(e) => setForm({ ...form, area_km2: +e.target.value })} style={inp} />
        <input type="number" step="0.1" placeholder="Line (km)" value={form.line_km || ''} onChange={(e) => setForm({ ...form, line_km: +e.target.value })} style={inp} />
        <input type="number" placeholder="Fold" value={form.fold || ''} onChange={(e) => setForm({ ...form, fold: +e.target.value })} style={inp} />
        <input type="number" step="0.1" placeholder="Resolution (m)" value={form.resolution_m || ''} onChange={(e) => setForm({ ...form, resolution_m: +e.target.value })} style={inp} />
        <button type="submit" style={{ background: '#7c3aed', color: '#fff', border: 'none', borderRadius: 8, padding: 10, fontWeight: 600, cursor: 'pointer' }}>Create Survey</button>
      </div>
      {msg && <p style={{ margin: '8px 0 0', color: '#7c3aed', fontSize: 13 }}>{msg}</p>}
    </form>
  )
}

const inp: React.CSSProperties = {
  background: '#0f0f1a',
  border: '1px solid #333',
  borderRadius: 8,
  padding: 10,
  color: '#e0e0e0',
  outline: 'none',
}
