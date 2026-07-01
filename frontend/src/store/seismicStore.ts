import { create } from 'zustand'
import axios from 'axios'
import { useAuthStore } from './authStore'

const api = axios.create({ baseURL: '/api' })

api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

interface Survey {
  id: string
  survey_name: string
  location: string
  survey_type: string
  area_km2: number
  status: string
  line_km: number
  fold: number
  resolution_m: number
  acquisition_date: string
  created_at: string
}

interface Prospect {
  id: string
  survey_id: string
  prospect_name: string
  volume_oil_mmboe: number
  volume_gas_bcf: number
  probability: number
  risk_level: string
  status: string
  created_at: string
}

interface Stats {
  total_surveys: number
  total_area_km2: number
  interpreting_count: number
  total_prospects: number
  drill_ready: number
  avg_probability: number
}

interface SeismicState {
  surveys: Survey[]
  prospects: Prospect[]
  stats: Stats | null
  loading: boolean
  fetchSurveys: () => Promise<void>
  fetchProspects: () => Promise<void>
  fetchStats: () => Promise<void>
  submitSurvey: (data: any) => Promise<void>
}

export const useSeismicStore = create<SeismicState>((set) => ({
  surveys: [],
  prospects: [],
  stats: null,
  loading: false,

  fetchSurveys: async () => {
    const { data } = await api.get('/surveys/')
    set({ surveys: data })
  },

  fetchProspects: async () => {
    const { data } = await api.get('/prospects/')
    set({ prospects: data })
  },

  fetchStats: async () => {
    const [sRes, pRes] = await Promise.all([
      api.get('/surveys/stats'),
      api.get('/prospects/stats'),
    ])
    set({ stats: { ...sRes.data, ...pRes.data } })
  },

  submitSurvey: async (formData: any) => {
    await api.post('/surveys/', formData)
  },
}))
