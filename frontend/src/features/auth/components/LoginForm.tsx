
function LoginForm(){

    return <div className='card'>
        <div className='card-body'>
            <h5 className='card-title'>
                Learning Management
            </h5>
            <form className="card-body">
              <div className="mb-3">
                <label className="form-label">Email</label>
                <input type="email" className="form-control" />
              </div>
              <div className="mb-3">
                <label className="form-label">Password</label>
                <input type="password" className="form-control" />
              </div>
              <button type="submit" className="btn btn-primary">Login</button>
            </form>
        </div>
    </div>;
}

export default LoginForm;