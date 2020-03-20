import React, { Component } from "react";
import { render } from "react-dom";
import Crud from './Crud';
import {Base64} from 'base64-js';
import MyModal from './Modal';
import './App.css';





  class App extends Component {
    constructor(props){
    super(props);
    this.state = {
        error: null,
        isLoaded: false,
        items: [],
        value:'',
        file:null,
<<<<<<< HEAD
        username:'chetan',
        password:'chetan1990',
        show:false,
        index:0,
=======
        username:'************',
        password:'********',
        show:false,
>>>>>>> f7796e4955d320e37b29f67241db6de5a0210fc7
        
      };
      this.handlePost= this.handlePost.bind(this);
    
    }
    
    handleClose = ()=>{
      this.setState({show:false});
<<<<<<< HEAD
  
    }

  
  handleShow = (index)=>{
      this.setState({show:true,index:index});
      console.log(index);
      
  }

=======
  }
  handleShow = ()=>{
      this.setState({show:true});
  }
>>>>>>> f7796e4955d320e37b29f67241db6de5a0210fc7
  
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
    }
  
    handlePost(){
      let fd = new FormData();
      fd.append('user',1);
      fd.append('text',this.state.value);
      fd.append('image',this.state.file);
    fetch("http://127.0.0.1:8000/api/status/All/",
      {method:'POST', 
      body:fd})
      .then(res=>res.json())
      .then((result)=>{
      this.setState({items:[...this.state.items,result]});
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
      
      console.log('hello me' );
      const itemsStatus= this.state.items.filter(c => c.id !== item.id);
      this.handleDelete(item.id)
      this.setState({ items:itemsStatus});
    

    }

    handleSubmit = (event)=>{
     
      alert('this is value : ' + this.state.value + this.state.file);
      event.preventDefault();
      this.handlePost();
      this.setState({value:'',file:'No File Choosen'})
     
    }

    handleChange= (event)=>{
      this.setState({value:event.target.value});

      
    }

handleFiles  = (event)=>{
<<<<<<< HEAD
  
  
  //let file = Array.from(files).forEach(file => this.setState({file:file})
 // );
this.setState({file:event.target.files[0]});


}
handleIndex = (item,index)=>{
  console.log(this.state.items[index]);
}
handleContent = (item,index)=>{
  const item1 = this.state.items.indexOf(item);
  
=======
  
  
  //let file = Array.from(files).forEach(file => this.setState({file:file})
 // );
this.setState({file:event.target.files[0]});


}
handleIndex = (item)=>{
  
  console.log(this.state.items.indexOf(item));
}
handleContent = (item)=>{
  const item1 = this.state.items.indexOf(item);
  
>>>>>>> f7796e4955d320e37b29f67241db6de5a0210fc7
 
}

handleText = (event) =>{
  console.log("Hello world" + event.target.value);
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

<div id="myForm1">
  
        <form id="myForm" onSubmit={this.handleSubmit} ref="myform">
          <label>
            Status:
            <textarea className="text-area offset-9" ref="text"  value={this.state.value} onChange={this.handleChange}/>
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
       
         
<<<<<<< HEAD
      <Crud onMe={this.handleMe} index={this.state.index} items ={this.state.items}  onPost={this.handlePost} onDelete={this.handleDelete} onUpdate={this.forceUpdate}  onText={this.handleText} onSubmit={this.handleSubmit} onFiles={this.handleFiles} file={this.state.file} value={this.state.value} handleShow={this.handleShow} handleClose={this.handleClose} show={this.state.show} handleContent={this.handleContent} handleIndex={this.handleIndex}/>
=======
      <Crud onMe={this.handleMe} items ={this.state.items}  onPost={this.handlePost} onDelete={this.handleDelete} onUpdate={this.forceUpdate}  onText={this.handleText} onSubmit={this.handleSubmit} onFiles={this.handleFiles} file={this.state.file} value={this.state.value} handleShow={this.handleShow} handleClose={this.handleClose} show={this.state.show} handleContent={this.handleContent} handleIndex={this.handleIndex}/>
>>>>>>> f7796e4955d320e37b29f67241db6de5a0210fc7
    
     
     
      
</React.Fragment>
        );
      }
    }
  }


export default App;

const container = document.getElementById("app");
render(<App />, container);
