import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="bg-gradient-to-r from-green-400 to-blue-500 min-h-screen">
      <div className="container mx-auto px-4 h-screen flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-6xl font-bold text-white mb-8 animate-bounce">
            Welcome to ShopIt
          </h1>

          <div className="flex space-x-6 justify-center">
            <Link
              to="/auth"
              state={{ initialForm: 'login' }}
              className="inline-block w-64 bg-white text-purple-600 font-semibold py-3 px-6 rounded-lg shadow-lg hover:bg-purple-100 transition-all duration-300 transform hover:scale-105"
            >
              Login
            </Link>

            <Link
              to="/auth"
              state={{ initialForm: 'signup' }}
              className="inline-block w-64 bg-opacity-20 bg-white backdrop-blur-lg text-white font-semibold py-3 px-6 rounded-lg shadow-lg hover:bg-opacity-30 transition-all duration-300 transform hover:scale-105 border-2 border-white"
            >
              Sign Up
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
