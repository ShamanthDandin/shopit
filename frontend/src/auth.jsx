import { useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';

const Auth = () => {
  const location = useLocation();
  const initialForm = location.state?.initialForm || 'login';

  const [isSignup, setIsSignup] = useState(initialForm === 'signup');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const toggleForm = () => setIsSignup(!isSignup);

  useEffect(() => {
    setIsSignup(initialForm === 'signup');
  }, [initialForm]);

  const handleSignup = (e) => {
    e.preventDefault();
    const role = 'customer'; // default role
    console.log('Sign Up:', { name, email, password, role });
    // TODO: send signup request
  };

  const handleLogin = (e) => {
    e.preventDefault();
    console.log('Login:', { email, password });
    // TODO: send login request
  };

  return (
    <div className="bg-gray-100 min-h-screen flex items-center justify-center">
      <div className="bg-white p-8 rounded shadow-md w-96">
        {isSignup ? (
          <>
            <h3 className="text-lg font-medium mb-2">Sign Up</h3>
            <form onSubmit={handleSignup}>
              <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2">Name</label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="shadow border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline"
                  required
                />
              </div>
              <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2">Email</label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="shadow border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline"
                  required
                />
              </div>
              <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2">Password</label>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="shadow border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline"
                  required
                />
              </div>
              <button
                type="submit"
                className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
              >
                Sign Up
              </button>
            </form>
            <p className="text-sm text-center mt-4">
              Already have an account?{' '}
              <button onClick={toggleForm} className="text-blue-600 hover:underline">
                Login
              </button>
            </p>
          </>
        ) : (
          <>
            <h3 className="text-lg font-medium mb-2">Login</h3>
            <form onSubmit={handleLogin}>
              <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2">Email</label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="shadow border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline"
                  required
                />
              </div>
              <div className="mb-6">
                <label className="block text-gray-700 text-sm font-bold mb-2">Password</label>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="shadow border rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline"
                  required
                />
              </div>
              <button
                type="submit"
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
              >
                Login
              </button>
            </form>
            <p className="text-sm text-center mt-4">
              Don't have an account?{' '}
              <button onClick={toggleForm} className="text-green-600 hover:underline">
                Sign Up
              </button>
            </p>
          </>
        )}
      </div>
    </div>
  );
};

export default Auth;
