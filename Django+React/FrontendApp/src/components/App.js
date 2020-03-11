import React, { Component } from "react";
import { render } from "react-dom";




  class App extends Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        isLoaded: false,
        items: [],
        handlePost:this.handlePost.bind(this),
        handleUpdate:this.handleUpdate.bind(this),
        handleDelete:this.handleDelete.bind(this),
      };
    }
  
    componentDidMount() {
      fetch("http://127.0.0.1:8000/api/status/All/")
        .then(res => res.json())
        .then(
          (result) => {
            console.log(result);
            this.setState({
              isLoaded: true,
              items: result
            });
          },
       
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }
 
    handlePost(){
      fetch("http://127.0.0.1:8000/api/status/All/",
      {method:'POST', 
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({user:1,"text":"hello"})})
      .then(res=>res.json())
      .then((result)=>{
        console.log("Success");
      })
      .catch((error)=>{
        console.log("error",error);
      })
    }

    handleUpdate(){
      fetch("http://127.0.0.1:8000/api/status/All/",
      {method:'PUT', 
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({id:8,user:1,"text":"hello world"})})
      .then(res=>res.json())
      .then((result)=>{
        console.log("Success");
      })
      .catch((error)=>{
        console.log("error",error);
      })
    }

    handleDelete(id){
      fetch("http://127.0.0.1:8000/api/status/All/?" + new URLSearchParams({'id':id}),
      {method:'DELETE', 
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify()})
      .then(res=>res.text())
      .then((result)=>{
        console.log("success",result);
      })
      .catch((error)=>{
        console.log("error",error);
      })
    }
    handleMe = (item)=>{
      const itemsStatus = this.state.items.filter(c => c.id !== item.id);
      this.handleDelete(item.id);
      this.setState({items:itemsStatus});
    }
 
  
    render() {
      const { error, isLoaded, items } = this.state;
      const listItems = 
    console.log(listItems);
     
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else {
        return (
          <React.Fragment>
          <button onClick={this.state.handlePost}>Create Me</button>
         
          <button onClick={this.state.handleDelete}>Delete Me</button>
          
          
         <ul>{this.state.items.map((item) =>
         <div className="card mb-3" style={{width:450}}>
          <div class="row no-gutters">
         <div className="col-md-4">
         <li><img src={item.image} style={{width:150,height:150}} className="card-img" alt={item.user}/>
      
      </li>
      </div>
      <div className="col-md-8">
      <div className="card-body">
        <h5 className="card-title">{item.user}</h5>
        <p className="card-text">{item.text}</p>
        <p className="card-text"><small className="text-muted">Last updated 3 mins ago</small></p>
          <button onClick={this.handleMe(item)}>Me</button>
 <button onClick={this.state.handleUpdate}>Update Me</button>
      </div>
      </div>

         </div>
          </div>
    
    )}
 
    </ul>
          
         
         
           </React.Fragment>
        );
      }
    }
  }


export default App;

const container = document.getElementById("app");
render(<App />, container);
