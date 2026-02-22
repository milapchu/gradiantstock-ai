import { useState } from 'react'
import './App.css'
import Register from './components/Register'
import Login from './components/Login'

function App() {
  // Simple state to toggle between Login and Register views
  const [isLoginView, setIsLoginView] = useState(true)

  return (
    <div className="app-container">
      <header>
        <h1>GradiantStock</h1>
        <p>Shop Inventory Management System</p>
      </header>

      <main className="card">
        {/* Toggle between components based on state */}
        {isLoginView ? <Login /> : <Register />}

        <div className="toggle-section">
          <p>
            {isLoginView ? "New shop?" : "Already have an account?"}
            <button
              className="link-button"
              onClick={() => setIsLoginView(!isLoginView)}
            >
              {isLoginView ? " Register here" : " Login here"}
            </button>
          </p>
        </div>
      </main>
    </div>
  )
}

export default App