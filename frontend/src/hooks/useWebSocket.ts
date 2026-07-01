import { useEffect, useRef } from 'react'
import { useWsStore } from '../store/wsStore'
import { useAuthStore } from '../store/authStore'

export function useWebSocket() {
  const wsRef = useRef<WebSocket | null>(null)
  const addEvent = useWsStore((s) => s.addEvent)
  const setConnected = useWsStore((s) => s.setConnected)
  const token = useAuthStore((s) => s.token)

  useEffect(() => {
    if (!token) return

    const protocol = location.protocol === 'https:' ? 'wss:' : 'ws:'
    const host = location.host
    const url = `${protocol}//${host}/ws/interpret`

    let reconnectTimeout: ReturnType<typeof setTimeout>

    function connect() {
      const ws = new WebSocket(url)
      wsRef.current = ws

      ws.onopen = () => setConnected(true)

      ws.onmessage = (e) => {
        const msg = JSON.parse(e.data)
        addEvent(msg.event, msg.data)
      }

      ws.onclose = () => {
        setConnected(false)
        reconnectTimeout = setTimeout(connect, 3000)
      }

      ws.onerror = () => ws.close()
    }

    connect()

    return () => {
      clearTimeout(reconnectTimeout)
      wsRef.current?.close()
    }
  }, [token])

  const send = (msg: object) => {
    wsRef.current?.send(JSON.stringify(msg))
  }

  return { send }
}
