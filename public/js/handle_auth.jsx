import ActionBlock from './action_block'

export default class HandleAuth extends React.Component {
    constructor(props){
        super(props);
    }
    
    componentDidMount(){
        const code = this.props.location.query.code;
        console.log(code);
    }
    
    render(){
        return (< ActionBlock link='/api/hashtag?tag="nofilter"' text='Say Hello World!' />);
    }
}
