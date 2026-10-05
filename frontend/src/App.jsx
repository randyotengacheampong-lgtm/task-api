import { useState, useEffect } from 'react';
const API = "http://127.0.0.1:8001"
function App() {
  const [user, setUser] = useState(() => localStorage.getItem('token')? { token: localStorage.getItem('token') } : null);
  const [view, setView] = useState('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');
  const [msg, setMsg] = useState('');
  const [doneMap, setDoneMap] = useState({});

  const getToken = () => localStorage.getItem('token');
  const authHeader = () => {
    const t = getToken();
    return t? { Authorization: `Bearer ${t}` } : {};
  };

  const safeMsg = (data) => {
    if (!data) return 'Unknown error';
    if (typeof data === 'string') return data;
    if (data.message && typeof data.message === 'string') return data.message;
    if (data.detail && typeof data.detail === 'string') return data.detail;
    if (data.errors) return JSON.stringify(data.errors);
    if (Array.isArray(data)) return JSON.stringify(data);
    return JSON.stringify(data);
  };

  const fetchTasks = async () => {
    try {
      const res = await fetch(`${API}/tasks`, { headers: authHeader() });
      const data = await res.json().catch(()=>[]);
      if (res.status === 401) { logout(); return; }
      if (!res.ok) throw new Error(safeMsg(data));
      setTasks(Array.isArray(data)? data : data.tasks || []);
    } catch (e) {
      setMsg('Tasks: ' + e.message);
    }
  };

  useEffect(() => { if (user) fetchTasks(); }, [user]);

  const register = async (e) => {
    e.preventDefault();
    setMsg('');
    try {
      const res = await fetch(`${API}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: email, password })
      });
      const data = await res.json().catch(()=>({}));
      if (!res.ok) throw new Error(safeMsg(data));
      setMsg('Registered! Now login.');
      setView('login');
    } catch (err) { setMsg(err.message); }
  };

  const login = async (e) => {
    e.preventDefault();
    setMsg('');
    try {
      const form = new URLSearchParams();
      form.append('username', email);
      form.append('password', password);
      const res = await fetch(`${API}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: form.toString()
      });
      const data = await res.json().catch(()=>({}));
      if (!res.ok) throw new Error(safeMsg(data));
      const token = data.access_token || data.token;
      if (!token) throw new Error('No token returned');
      localStorage.setItem('token', token);
      setUser({ token });
    } catch (err) { setMsg(err.message); }
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
    setView('login');
  };

  const addTask = async (e) => {
    e.preventDefault();
    if (!newTask.trim()) return;
    try {
      const res = await fetch(`${API}/tasks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json',...authHeader() },
        body: JSON.stringify({
          title: newTask,
          description: newTask,
          content: newTask,
          name: newTask,
          text: newTask
        })
      });
      const data = await res.json().catch(()=>({}));
      if (!res.ok) throw new Error(safeMsg(data));
      setNewTask('');
      fetchTasks();
    } catch (err) { setMsg(err.message); }
  };

  const deleteTask = async (id) => {
  setMsg('');
  try{
    const res = await fetch(`${API}/tasks/${id}`, { method: 'DELETE', headers: authHeader() });
    if(!res.ok) throw new Error('Delete failed');
    fetchTasks();
  }catch(err){
    setMsg('');
    setTasks(prev => prev.filter(t => t.id!== id));
  }
};

  const toggleDone = (id) => {
    setDoneMap(prev => ({...prev, [id]:!prev[id]}));
  };

  if (!user) {
    return (
      <div style={{ padding: 40, background: '#0a0a2a', minHeight: '100vh', color: 'white', textAlign: 'center' }}>
        <div style={{ background:'#1a1a3a', padding:32, borderRadius:16, maxWidth:400, margin:'0 auto' }}>
          <h1>TaskFlow ✨</h1>
          <h3 style={{color:'#ccc'}}>{view === 'login'? 'Login' : 'Register'}</h3>
          <form onSubmit={view === 'login'? login : register}>
            <input placeholder="username" value={email} onChange={e=>setEmail(e.target.value)} style={{margin:5, padding:10, borderRadius:8, border:'none', width:'90%'}} /><br/>
            <input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} style={{margin:5, padding:10, borderRadius:8, border:'none', width:'90%'}} /><br/>
            <button type="submit" style={{margin:5, padding:'10px 20px', borderRadius:8, border:'none', background:'#5b5bff', color:'white', fontWeight:700}}>{view==='login'?'Login':'Register'}</button>
          </form>
          <p style={{color:'yellow', whiteSpace:'pre-wrap'}}>{msg}</p>
          <a href="#" onClick={()=>setView(view==='login'?'register':'login')} style={{color:'#60a5fa'}}>
            {view==='login'?'No account? Register':'Have account? Login'}
          </a>
        </div>
      </div>
    );
  }

  return (
    <div style={{ padding: 40, background: '#0a0a2a', minHeight: '100vh', color: 'white' }}>
      <div style={{display:'flex', justifyContent:'space-between'}}><h2>My Tasks 🎯</h2><button onClick={logout} style={{padding:'8px 14px', borderRadius:8, border:'none', background:'#2a2a4a', color:'white'}}>Logout</button></div>
      {msg && <p style={{color:'yellow'}}>{msg}</p>}
      <form onSubmit={addTask} style={{display:'flex', gap:10, marginTop:16}}>
        <input value={newTask} onChange={e=>setNewTask(e.target.value)} placeholder="New task" style={{padding:12, width:350, borderRadius:8, border:'none'}}/>
        <button style={{padding:'0 20px', borderRadius:8, border:'none', background:'#5b5bff', color:'white', fontWeight:700}}>Add</button>
      </form>
      <ul style={{marginTop:20, listStyle:'none', padding:0}}>
        {tasks.map((t,i)=>{
          const title = t.title || t.description || t.content || t.name || t.text || `Task ${t.id}`;
          const isBroken =!t.title &&!t.description &&!t.content &&!t.name &&!t.text;
          if (isBroken) return null;
          const isDone = doneMap[t.id];
          return (
            <li key={t.id||i} style={{margin:'12px 0', background: isDone? '#1a3a2a' : '#1a1a3a', padding:'12px 14px', borderRadius:10, display:'flex', justifyContent:'space-between', alignItems:'center', borderLeft: isDone? '4px solid #22c55e' : '4px solid #5b5bff'}}>
              <label style={{display:'flex', alignItems:'center', gap:10}}>
                <input type="checkbox" checked={!!isDone} onChange={()=>toggleDone(t.id)} style={{width:20, height:20, accentColor:'#22c55e'}}/>
                <span style={{textDecoration: isDone?'line-through':'none', color: isDone?'#9ca3af':'white', fontWeight:600}}>{title}</span>
              </label>
              <button onClick={()=>deleteTask(t.id)} style={{background:'#ff4444', color:'white', border:'none', padding:'6px 12px', borderRadius:8, cursor:'pointer', fontWeight:600}}>Delete</button>
            </li>
          );
        })}
        {tasks.filter(t=>t.title || t.description || t.content || t.name || t.text).length===0 && <li style={{color:'#888', marginTop:30}}>No tasks yet</li>}
      </ul>
    </div>
  );
}
export default App;