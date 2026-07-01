import { useEffect } from 'react'
import Layout from '../components/Layout'
import StatsCards from '../components/StatsCards'
import SurveyForm from '../components/SurveyForm'
import SurveyList from '../components/SurveyList'
import ProspectList from '../components/ProspectList'
import InterpretationFeed from '../components/InterpretationFeed'
import { useSeismicStore } from '../store/seismicStore'
import { useWebSocket } from '../hooks/useWebSocket'

export default function Dashboard() {
  const fetchSurveys = useSeismicStore((s) => s.fetchSurveys)
  const fetchProspects = useSeismicStore((s) => s.fetchProspects)
  const fetchStats = useSeismicStore((s) => s.fetchStats)
  const stats = useSeismicStore((s) => s.stats)
  useWebSocket()

  useEffect(() => {
    fetchSurveys()
    fetchProspects()
    fetchStats()
  }, [])

  return (
    <Layout>
      <StatsCards stats={stats} />
      <SurveyForm />
      <InterpretationFeed />
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24 }}>
        <SurveyList />
        <ProspectList />
      </div>
    </Layout>
  )
}
