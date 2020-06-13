import React, { Component, createRef,ReactDOM } from "react";
import { Card , Button} from "react-bootstrap";


class UserProfile extends Component{

    render(){
      console.log("props",this.props.profile);
   

        return (
            <Card style={{ width: '18rem',marginTop:10}}>
  <Card.Img variant="top" src={this.props.profile.image}/>
  <Card.Body>
    <Card.Title>{this.props.profile.username}</Card.Title>
    <Card.Text>
  <p>Name: {this.props.profile.first_name} {this.props.profile.last_name}</p>
  <p>Contact info: {this.props.profile.email}</p>
    </Card.Text>
    <Button variant="primary">Go somewhere</Button>
  </Card.Body>
</Card>
        );
    }
}
export default UserProfile;