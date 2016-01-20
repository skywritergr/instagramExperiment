import LoginButton from './button'

class App extends React.Component{
    render(){
        return (
            <div>
                {this.props.children || <LoginButton />}
            </div>   
        );
    };
}

module.exports = App;