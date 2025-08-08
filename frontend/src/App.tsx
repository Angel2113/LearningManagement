import LoginForm from "./features/auth/components/LoginForm";

function App() {
    return <div className="container-fluid">
        <div className='row justify-content-center min-vh-100'>
            <div className='col-2'/>
            <div className='col-8'>
                <LoginForm />
            </div>
            <div className='col-2'/>
        </div>
    </div>
}

export default App;