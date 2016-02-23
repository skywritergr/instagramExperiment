import ActionBlock from './action_block'

export default class HandleAuth extends React.Component {
    constructor(props){
        super(props);
    }
    
    componentDidMount(){
        const code = this.props.location.query.code;
    }
    
    render(){
        return (
            <div>
                <input className="form-control" type="text" placeholder="Choose a hashtag"/>
                <div className="actionContainer">
                    <ActionBlock link='/api/likephotos?tag="nofilter"' type='GET' text='Like 15 photos' />
                    <ActionBlock link='/api/leavecomments' type='POST' text='Leave comment to 15 photos' />
                    <ActionBlock link='/api/followusers?tag="project365"' type='GET' text="follow users!" />
                </div>
            </div>
            );
    }
}
