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
        return (
            <div>
            <ActionBlock link='/api/likephotos?tag="nofilter"' text='Like 15 photos' />
            <ActionBlock link='/api/leavecomments?tag="project365"&comment="Nice picture! :)"' text='Leave comment to 15 photos' />
            <ActionBlock link='/api/followusers?tag="project365"' text="follow users!" />
            </div>
            );
    }
}
