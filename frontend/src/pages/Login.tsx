import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import axios from 'axios'
import { useAuthStore } from '../store/authStore'

export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()
  const setAuth = useAuthStore((s) => s.setAuth)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const { data } = await axios.post('/api/auth/login', { email, password })
      setAuth(data.access_token, data.user)
      navigate('/')
    } catch {
      setError('Invalid credentials')
    }
  }

  return (
    <div style={{ minHeight: '100vh', background: '#0f0f1a', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <form onSubmit={handleSubmit} style={{ background: '#1a1a2e', border: '1px solid #7c3aed44', borderRadius: 16, padding: 40, width: 360 }}>
        <h1 style={{ color: '#7c3aed', textAlign: 'center', marginBottom: 24 }}>SeismicAI</h1>
        <h3 style={{ color: '#e0e0e0', textAlign: 'center', marginBottom: 20 }}>Sign In</h3>
        <input placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required style={inp} />
        <input placeholder="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required style={{ ...inp, marginTop: 12 }} />
        {error && <p style={{ color: '#ef4444', fontSize: 13 }}>{error}</p>}
        <button type="submit" style={{ ...btn, marginTop: 16 }}>Login</button>
        <p style={{ textAlign: 'center', marginTop: 16, fontSize: 13, color: '#999' }}>
          Don't have an account? <Link to="/register" style={{ color: '#7c3aed' }}>Register</Link>
        </p>
      </form>
    </div>
  )
}

const inp: React.CSSProperties = {
  width: '100%',
  background: '#0f0f1a',
  border: '1px solid #333',
  borderRadius: 8,
  padding: 12,
  color: '#e0e0e0',
  outline: 'none',
  boxSizing: 'border-box',
}

const btn: React.CSSProperties = {
  width: '100%',
  background: '#7c3aed',
  color: '#fff',
  border: 'none',
  borderRadius: 8,
  padding: 12,
  fontWeight: 600,
  cursor: 'pointer',
}
