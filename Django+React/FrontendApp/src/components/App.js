import React, { Component, createRef } from "react";
import { render } from "react-dom";
import Crud from './Crud';
import { Base64 } from 'base64-js';
import MyModal from './Modal';
import './App.css';
import { FaBeer } from 'react-icons/fa';
import { Navbar, NavItem } from "react-bootstrap";
import Cookies from 'universal-cookie';



class App extends Component {
  constructor(props) {
    super(props);
    this.localVideo =React.createRef();
    this.state = {
      error: null,
      isLoaded: false,
      items: [],
      value: '',
      file: null,
      username: 'chetan0000',
      password: 'abcdefghijk',
      show: false,
      index: 0,
      Users :[],
      send_requests:[],
      get_requests:[],
      already_send:false,
      

    };
    this.handlePost = this.handlePost.bind(this);

  }



  handleClose = () => {
    this.setState({ show: false });

  }


  handleShow = (index, id) => {
    this.setState({ show: true, index: index });
    console.log(index);
    console.log(id);

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
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
      fetch("http://127.0.0.1:8000/api/status/requests/",{
        credentials:'include',
        method:'GET',
        headers:{'Content-Type':'application/json','Authorization':'Basic' + btoa(this.state.username+":"+this.state.password)}
  
      })
        .then(res => res.json())
        .then((result) => {
          
        console.log(result[1])
         var  get_req= JSON.parse(result[1])
         
       
          this.setState({
            send_requests:result[0],
            get_requests:get_req
          })
        
          /*
          result.map(user=>{
            var users = this.state.Users.filter(u=>u[1]==user.fields.to_user);
            this.setState({requests:[...this.state.requests ,users[0]]})
            
          })
          */
        }) 
        .catch((error) => {
          console.log("error", error);
        })
  }

  handlePost() {
    let fd = new FormData();
    fd.append('user', 1);
    fd.append('text', this.state.value);
    fd.append('image', this.state.file);
    fetch("http://127.0.0.1:8000/api/status/All/",
      {
        method: 'POST',
        body: fd
      })
      .then(res => res.json())
      .then((result) => {
        this.setState({ items: [...this.state.items, result] });
      })
      .catch((error) => {
        console.log("error", error);
      })
  }





  handleUpdate(id) {
    let fd = new FormData();
    fd.append('user', 1);
    fd.append('text', this.state.value);
    fd.append('image', this.state.file);
    fetch("http://127.0.0.1:8000/api/status/All/?" + new URLSearchParams({ 'id': id }),
      {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "user": 1, "text": this.state.value })
      })
      .then(res => res.json())
      .then((result) => {
        const items = this.state.items;
        items.map((item) => {
          if (item.id == result.id) {
            item.text = result.text;
          }
        })
        this.setState({ items: items });



        console.log(result);
      })
      .catch((error) => {
        console.log("error", error);
      })
  }






  handleDelete(id) {

    fetch("http://127.0.0.1:8000/api/status/All/?" + new URLSearchParams({ 'id': id }),
      {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify()
      })
      .then(res => res.text())
      .then((result) => {
        console.log("success", result);
      })
      .catch((error) => {
        console.log("error", error);
      })
  }




  handleMe = (item) => {

    console.log('hello me');
    const itemsStatus = this.state.items.filter(c => c.id !== item.id);
    this.handleDelete(item.id)
    this.setState({ items: itemsStatus });


  }





  handleSubmit = (event) => {

    alert('this is value : ' + this.state.value + this.state.file);
    event.preventDefault();
    this.handlePost();
    //this.setState({value:'',file:'No File Choosen'})

  }

  handleChange = (event) => {
    this.setState({ value: event.target.value });

  }


  handleEdit = (refs, event, props) => {

    //console.log(id);
    event.preventDefault();
    console.log(refs.textInput.value);
    const t = refs.textInput.value;
    this.setState({ value: t });



  }


handleUsers = ()=>{
  fetch("http://127.0.0.1:8000/api/").then(res=>
  res.json()
).then(result=>{
 
  this.state.send_requests.forEach((request)=>{
    var data = result.filter(c=>c[1]==request)
    

  })

  
  this.setState({
    
    Users:result
  })
},error=>{
  console.log(error);
})
}

  handleFiles = (event) => {


    //let file = Array.from(files).forEach(file => this.setState({file:file})
    // );
    this.setState({ file: event.target.files[0] });


  }


  handleIndex = (item, index) => {
    console.log(this.state.items[index]);
  }


  handleContent = (item, index) => {
    const item1 = this.state.items.indexOf(item);


  }

  handleText = (event) => {
    console.log("Hello world" + event.target.value);
  }
  handleIt = (id) => {
    this.handleUpdate(id);
    this.setState({ show: false });
    this.setState({ value: '' });
  }
  handleAddFriend = (index)=>{ 
    const cookies = new Cookies();

    var csrftoken = cookies.get('csrftoken');
    console.log("csrftoken",cookies)
  
console.log(this.state.Users[index][1])
var id = this.state.Users[index][1]

fetch("http://127.0.0.1:8000/api/status/add/",
      {
        method: 'POST',
        mode:'cors',
        headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
        credentials:'include',
        body:JSON.stringify({'id':id,'username':'chetan0000','password':'abcdefghijk'})

      })
      .then(res => res.json())
      .then((result) => {
        console.log(result.length)
        /*
        this.setState({requests:result})
        console.log('requests',this.state.requests)
        */
      }) 
      .catch((error) => {
        console.log("error", error);
      })
  }
  handleFreiendRequests=()=>{
    
  }
  render() {
  
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    }
    else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <React.Fragment >
        <Navbar >
            <button className="btn btn-info" onClick={this.handleUsers} style={{marginRight:10}}>Users</button>
            <button type="button"  className="btn btn-primary"  style={{marginRight:10}}  data-toggle="collapse" data-target="#collapsebutton"  onClick={()=>this.handleFreiendRequests} >
             send requests<span className="badge badge-light"> {this.state.send_requests.length}</span>
             </button>
             <button type="button"  className="btn btn-primary"  data-toggle="collapse" data-target="#collapsebutton1" >
             get requests<span className="badge badge-light"> {this.state.get_requests.length}</span>
             </button>
            </Navbar>
             <div className="list-group"><ul style={{marginLeft:10 }}>{this.state.Users.map((user,index)=>
             <div className="card mb-3 offset-4"  style={{marginLeft:20 , width:200 }}>
          
             <div class="row no-gutters"  >
          
   
          
          <p className="card-text text-primary font-weight-bold mb-2"  style={{marginRight:5}} st >{user}</p>
       
            {/*<p className="card-text mb-2">{item.id}<small className="text-muted">Last updated 3 mins ago</small></p>*/}
            <button onClick={()=>this.handleAddFriend(index)} data-toggle="button" className="btn btn-light">add</button>
       
    
      
    
             </div>
             
             </div>
            
             )}</ul></div>
             
             
             <div className="list-group"><ul style={{marginLeft:10 }}>{this.state.send_requests.map((user,index)=>
             <div className="card mb-3 offset-4"  style={{marginLeft:20 , width:200 }}>
          
             <div class="row no-gutters"  >
          
   
          
          <p className="card-text text-primary font-weight-bold mb-2"  style={{marginRight:5}} st >{user}</p>
       
            {/*<p className="card-text mb-2">{item.id}<small className="text-muted">Last updated 3 mins ago</small></p>*/}
            <button data-toggle="button" className="btn btn-light">cancel</button>
       
    
      
    
             </div>
             
             </div>
            
             )}</ul></div>
               
             {this.state.get_requests.map(user=>{
               <li>{user.fields.username}</li>
             })}
             {/*<div><video ref={this.localVideo}></video></div>*/}
          
          <div id="myForm1">

            <form id="myForm" onSubmit={this.handleSubmit} ref="myform">
              <label>
                Status:
            <textarea className="text-area offset-9" ref="text" value={this.state.value} onChange={this.handleChange} />
                <input type="file" className="form-control-file " ref="file" onChange={this.handleFiles} />

              </label>
              <input type="submit" value="Submit" />
            </form>
          </div>


          {/*
        <div className="card offset-4" style= {{width:450 , height:150 ,marginLeft:400 }
      <div class="md-form">
        <i class="fas fa-pencil-alt prefix grey-text"></i>
        <textarea id="form107" class="md-textarea form-control" rows="5"></textarea>
      </div>
      <div class="col-md-6">
      <input type="submit" value="Submit" style={{marginLeft:10}}/>
      </div>
      </div>
        */}


          <Crud handleIt={this.handleIt} onEdit={this.handleEdit} onMe={this.handleMe} index={this.state.index} items={this.state.items} onPost={this.handlePost} onDelete={this.handleDelete} onUpdate={this.handleUpdate} onText={this.handleText} onSubmit={this.handleSubmit} onFiles={this.handleFiles} file={this.state.file} value={this.state.value} handleShow={this.handleShow} handleClose={this.handleClose} show={this.state.show} handleContent={this.handleContent} handleIndex={this.handleIndex} />
         
        </React.Fragment>
      );
    }
  }
}


export default App;

const container = document.getElementById("app");
render(<App />, container);