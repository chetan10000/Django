import React, { Component, createRef } from "react";
import { render } from "react-dom";
import Crud from './Crud';
import { Base64 } from 'base64-js';
import MyModal from './Modal';
import './App.css';
import { FaBeer } from 'react-icons/fa';
import { Navbar, NavItem } from "react-bootstrap";
import Cookies from 'universal-cookie';
import UserProfile from './UserProfile';


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
	  profile:[],
      

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
  handleCancelRequest = (id)=>{
    var cookies = new Cookies();
    var csrftoken = cookies.get('csrftoken');
    var id=id;
    fetch("http://127.0.0.1:8000/api/status/cancel/",{
      method:'POST',
      mode:'cors',
      headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
      credentials:"include",
      body:JSON.stringify({'id':id,'username':this.state.username,'password':this.state.password})
    }).then(res=>res.json()).then(result=>{
      this.setState({send_requests:result});
    })
    .catch(e=>{
      console.log(e);
    })

  }
  handleRemoveFreind = (id)=>{
    console.log(id)
var cookies = new Cookies();
var csrftoken = cookies.get('csrftoken');
var id=id;
fetch ("http://127.0.0.1:8000/api/status/remove/",{
  method:'POST',
  mode:'cors',

  headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
    credentials:'include',
  body:JSON.stringify({'id':id,'username':this.state.username ,'password':this.state.password})

}).then(res=>res.json()) .then(result=>{
  console.log(result)
})
.catch(e=>{
  console.log(e)
})
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
            <button type="button"  className="btn btn-primary"   id="users" style={{marginLeft:10}} >
             Users
             </button>
             <button type="button"  className="btn btn-primary"   id="send_requests" style={{marginLeft:10}} >
             send requests<span className="badge badge-light"> {this.state.send_requests.length}</span>
             </button>
             <button type="button"  className="btn btn-primary"   id="get_requests" style={{marginLeft:10}} >
             get requests<span className="badge badge-light"> {this.state.get_requests.length}</span>
             </button>
             <button type="button"  className="btn btn-primary"   id="friends" style={{marginLeft:10}} >
             Friends<span className="badge badge-light"> {this.state.friends.length}</span>
             </button>
            
      
  </Navbar>
  <div>
<UncontrolledCollapse toggler="#friends">
<div className="list-group"><ul style={{marginLeft:330 }}>{this.state.friends.map((friend,index)=>
  <Card style={{width:300}}>
  <CardBody>
{
<p>
{friend.fields.username}
<button onClick={()=>this.handleRemoveFreind(friend.pk)}  className="btn btn-danger" style={{marginLeft:10}}>Remove</button>
</p>

}
</CardBody>
</Card>)}
</ul>
</div>
</UncontrolledCollapse>
</div>
<div>
<UncontrolledCollapse toggler="#users">
<div className="list-group"><ul style={{marginLeft:10 }}>{this.state.Users.map((user,index)=>
  <Card style={{width:300}}>
  <CardBody>
{
<p>
{user}
<button onClick={()=>this.handleAddFriend(index)} data-toggle="button" className="btn btn-primary" style={{marginLeft:10}}>add</button>
</p>

}
</CardBody>
</Card>)}
</ul>
</div>
</UncontrolledCollapse>
</div>
<div>
<UncontrolledCollapse toggler="#send_requests">
<div className="list-group"><ul style={{marginLeft:330 }}>{this.state.send_requests.map((user,index)=>
  <Card style={{width:300}}>
  <CardBody>
{

<p className="card-text text-primary font-weight-bold mb-2"  style={{marginRight:5,marginTop:10}} >{user.fields.username}
<button data-toggle="button" className="btn btn-primary" style={{margin:5}}  onClick={()=>{this.handleCancelRequest(user.pk)}} >cancel FreidnRequest</button>

</p>

}
</CardBody>
</Card>)}
</ul>
</div>
</UncontrolledCollapse>
</div>
<div>
<UncontrolledCollapse toggler="#get_requests">
<div className="list-group"><ul style={{marginLeft:330 }}>{this.state.get_requests.map((user,index)=>
  <Card style={{width:300}}>
  <CardBody>
{

<p className="card-text text-primary font-weight-bold mb-2"  style={{marginRight:5,marginTop:10}} >{user.fields.username}
<button data-toggle="button" className="btn btn-primary" style={{margin:5}}  onClick={()=>this.handleAcceptRequest(user.pk)} >accept</button>
<button data-toggle="button" className="btn btn-danger" style={{margin:5}} onClick={()=>this.handleRejectRequest(user.pk)}>reject</button>
       
</p>

}
</CardBody>
</Card>)}
</ul>
</div>
</UncontrolledCollapse>
<UserProfile profile={this.state.profile}/>
</div>
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