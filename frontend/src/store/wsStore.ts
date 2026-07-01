import { create } from 'zustand'

interface WsState {
  events: { event: string; data: unknown; timestamp: number }[]
  connected: boolean
  addEvent: (event: string, data: unknown) => void
  setConnected: (v: boolean) => void
  clear: () => void
}

export const useWsStore = create<WsState>((set) => ({
  events: [],
  connected: false,
  addEvent: (event, data) =>
    set((s) => ({
      events: [...s.events.slice(-99), { event, data, timestamp: Date.now() }],
    })),
  setConnected: (v) => set({ connected: v }),
  clear: () => set({ events: [] }),
}))
