import { Link } from "react-router-dom";
import {Form, Button} from 'react-bootstrap';

const PreviousButton = () => {
    return (
      <Link to={`/`}>
     <style type="text/css">
        {`
    .btn-flat {
      background-color: purple;
      color: white;
    }
    `}
      </style>
      <Button variant="flat">
      <div className="previous">
        back
      </div>
      </Button>
    </Link>
    );
  };
  
  export default PreviousButton;