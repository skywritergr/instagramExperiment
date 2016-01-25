var request = require('superagent');

export default class ActionBlock extends React.Component {
    constructor(props){
        super(props);
    }
    
    callAPI = () => {
        const link = this.props.link;
        const ajaxType = this.props.type;
        
        if(ajaxType==='GET'){
            request.get(link)
            .end(function(err, res){
                console.log(res);
            });    
        } else if(ajaxType==='POST'){
            request.post(link)
                .send({tag: 'project365', comment: 'Cool! :)'})
                .end(function(err, res){
                    console.log(res);
                });
        }
    };
    
    render(){
        return (
            <div className="actionBlock" onClick={this.callAPI}>
            {this.props.text}
            </div>
        );       
    }
}