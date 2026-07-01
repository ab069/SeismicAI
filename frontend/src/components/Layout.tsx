import { useAuthStore } from '../store/authStore'

export default function Layout({ children }: { children: React.ReactNode }) {
  const user = useAuthStore((s) => s.user)
  const logout = useAuthStore((s) => s.logout)

  return (
    <div style={{ minHeight: '100vh', background: '#0f0f1a', color: '#e0e0e0' }}>
      <header
        style={{
          background: '#7c3aed',
          padding: '16px 24px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <h1 style={{ margin: 0, fontSize: 24, color: '#fff' }}>SeismicAI</h1>
        <div style={{ display: 'flex', gap: 16, alignItems: 'center' }}>
          <span>{user?.name}</span>
          <button
            onClick={logout}
            style={{
              background: 'transparent',
              border: '1px solid #fff',
              color: '#fff',
              padding: '6px 14px',
              borderRadius: 6,
              cursor: 'pointer',
            }}
          >
            Logout
          </button>
        </div>
      </header>
      <main style={{ padding: 24 }}>{children}</main>
    </div>
  )
}
