import { Link } from "react-router-dom";
const Welcome = () => {
    return (
      <Link to={`/welcome`} className="pet">
      <div className="info">
        <h1>a welcome</h1>
      </div>
    </Link>
    );
  };
  
  export default Welcome;