export default class HandleAuth extends React.Component {
    constructor(props){
        super(props);
    }
    
    componentDidMount(){
        const code = this.props.location.query.code;
        console.log(code);
    }
    
    render(){
        return (<div><h3>Handled!</h3></div>);
    }
}