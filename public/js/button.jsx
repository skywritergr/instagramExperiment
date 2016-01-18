var request = require('superagent');

export default class LoginButton extends React.Component {
     constructor(props){
         super(props);
         this.state = {link:'#'};
     }
    
    getAuthLink = () => {
        var that = this;
        request.get('/get_url')
            .end(function(err, res){
                that.setState({link: res.body.url});
            })
    };
    
    goToInstagramLink = () => {
        window.location = this.state.link;
    };
    
    componentDidMount() {
        this.getAuthLink();
    }

    render() {
        console.log(decodeURIComponent(this.state.link));
        return (
            <button onClick={this.goToInstagramLink}>Login with Instagram</button>
        );
    }
}