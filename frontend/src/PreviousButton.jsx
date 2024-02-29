import { Link } from "react-router-dom";
import {Form, Button} from 'react-bootstrap';

const PreviousButton = () => {
    return (
      <Link to={`/`}>
      <Button>
      <div className="previous">
        back
      </div>
      </Button>
    </Link>
    );
  };
  
  export default PreviousButton;