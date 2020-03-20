import React ,{Component} from 'react';
import {Modal , Button} from 'react-bootstrap'
import Form from './Form';
class Crud extends Component{
    
    render(){
        const item = this.props.items.map((item)=>{
            item
        })
        console.log(typeof this.props.items[this.props.index]);

        return(
            <div id="myApp">
            
            <ul className="list-group list-group-flush">{this.props.items.map((item,index) =>
            <div className="card mb-3 offset-4" id="myCard" style={{marginLeft:20}}>
          
                <div class="row no-gutters">
                <div className="col-md-4">
            <img src={item.image} style={{width:150,height:150}} className="card-img" alt={item.user}/>
               
           
             
             </div>
             <div className="col-md-8 ">
             <div className="card-body">
               {/*<h5 className="card-title text-info font-weight-bold mb-2">{item.user}</h5>*/}
               <p className="card-text text-primary font-weight-bold mb-2">{item.text}</p>
               {/*<p className="card-text mb-2">{item.id}<small className="text-muted">Last updated 3 mins ago</small></p>*/}
               <button onClick ={()=>this.props.handleShow(index)} className="btn btn-light btn-sm m-2">Update</button>
               <button onClick ={this.props.onDelete} className="btn btn-danger btn-sm m-2">Delete</button>
               <button onClick ={() => {this.props.onMe(item)}} className="btn btn-info btn-sm m-2">Me</button>
               {/*<Form handleShow={this.props.handleShow} handleClose ={this.props.handleClose} show={this.props.show} items={this.props.items} />*/}
               
       
             </div>
             </div>
       
                </div>
                
                </div>
           )}
        
           </ul>
   
         
           
            <Modal show={this.props.show} onHide={this.props.handleClose}>
           <Modal.Header closeButton>
             <Modal.Title>Modal heading</Modal.Title>
           </Modal.Header>

           <li><Modal.Body>
            
            <textarea className="text-area" defaultValue={this.props.items[this.props.index].text} onChange={this.handleChange}/>
            </Modal.Body></li>
            <Modal.Footer>
             <Button variant="secondary" onClick={this.props.handleClose}>
               Close
             </Button>
             <Button variant="primary" onClick={this.props.handleClose}>
               Save Changes
             </Button>
           </Modal.Footer>
         </Modal>
           
           </div>
           
          
        );
    }
}
export default Crud;