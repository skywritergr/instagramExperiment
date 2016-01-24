var request = require('superagent');

export default class ActionBlock extends React.Component {
    constructor(props){
        super(props);
    }
    
    callAPI = () => {
        const link = this.props.link;
        
        request.get(link)
            .end(function(err, res){
                console.log(res);
            });
    };
    
    render(){
        return (
            <div className="actionBlock" onClick={this.callAPI}>
            {this.props.text}
            </div>
        );       
    }
}