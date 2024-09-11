import './style/topBar.css'

const TopBar = () =>{
    return (
        <div className="topBar_container">
            <div>
            <h1>Welcome To My TODO_LIST</h1> </div>
            <ul className='topbar_list'>
                <li className='list_item'>Home</li>
                <li className='list_item'>About</li>
                <li className='list_item'>Contact Us</li>
            </ul>
        </div>

    )
}

export default TopBar;