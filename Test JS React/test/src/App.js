import { useState } from 'react';
import './App.css';
import arrowDown from './media/arrow-down.png'
import arrowLeft from './media/arrow-left.png'
import arrowRight from './media/arrow-right.png'
import circle from './media/circle.png'
import circle_full from './media/circle_full.png'


function App() {
  // Simple Search
  var list = ['Apple', 'Banana', 'Orange', 'Lemon', 'Avocado', 'Eggplant', 'Tomato', 'Zucchini']
  const[search, setSearch] = useState('')

  //
  // Counter
  const[count, setCount] = useState(0)
  //
  // Accordion
  function Toggle(index){
    var current = document.getElementById(`content_display${index}`)
    console.log(index)
    if (current.style.display === 'none'){
    current.style.display = 'flex'
    }
    else{
      current.style.display = 'none'
    }
  }
  var list_dict = [{
    'title': 'Hello World', 'content':'This accordion says Hello !'
  }, {'title':'I am a cat', 'content':'Meooowww'}, {'title':'React is Amazing', 'content':'React is a JS library built by Facebook and allows devs to create interactive fluid user interfaces'}]

  //
  // Slider
  var list_images= ['./media/colombia.jpg','./media/ethiopia.jpg','./media/iceland.jpg','./media/scotland.jpg','./media/slovenia.jpg']
  const[counter, setCounter] = useState(0)
  //
  // Checkbox
  const[checkOne,setCheckOne]= useState(false)
  const[checkTwo,setCheckTwo]= useState(false)
  //
  //Login
  const[username,setUsername]=useState('')
  const[password,setPassword]=useState('')
  const[loggedIn, setLoggedIn]=useState(false)
  let list_users = [{
    'username':'Dadinho83','password':'HelloWorld'
  }, {'username':'ElDadz', 'password':'ReactIsTheBest'}]
  function handleSubmit(){
    for (let i = 0; i < list_users.length-1; i++){
      if (list_users[i].username == username){
        if(list_users[i].password == password){
          setLoggedIn(true)
          break
        }
        alert("Wrong Password, try again")
        break
      }
      alert("Username doesn't exist in Database")
    }
  }
  return (
    <>
    <div className='SimpleSearch'>
      <label htmlFor='search'>Search:</label>
      <input name='search' type='text' value={search} onChange={(event) => setSearch(event.target.value)} />
    </div>
    <div className='SimpleSearch'>
      {search ?
      <ul>
      {list.filter((element) => {
        return element.includes(`${search}`)
      }).map((element) => (
        <li>{element}</li>
      ))}
      </ul>
      : null}
    </div>
    <br></br>
    <div id='Counter'>
        {count}
        <br></br>
        <button onClick={() => setCount((prevCount) => prevCount + 1)}>Increment</button>
        {count === 0 ? null :
        <button onClick={() => setCount((prevCount) => prevCount - 1)}>Decrement</button>
        }
    </div>
    <br></br>
    <div id='DisplayList'>
      <ul>
        {list.map((element) =>(
          <li>{element}</li>
        ))}
      </ul>
    </div>
    <br></br>
    <div id='Accordion'>
      {list_dict.map((element, index) => (
        <>
        <div className='title_display' style={{backgroundColor:'grey', display:'flex',justifyContent:'space-between', padding:'10px', height:'80px', alignItems:'center',border:'1px solid black'}}>
          <h3>{element.title}</h3>
          <img alt='arrow-icon' src={arrowDown} style={{height:'30%'}} onClick={() => Toggle(index)}/>
        </div>
        <div id={`content_display${index}`} style={{backgroundColor:'lightgrey', padding:'10px', height:'80px', display:'none', alignItems:'center'}}>
          <h4>{element.content}</h4>
        </div>
        </>
      ))}
    </div>
    <br></br>
    <div id='Slider' style={{display:'flex',alignItems:'center', justifyContent:'center', margin:'20px auto', position:'relative'}}>
        <img src={arrowLeft} alt='arrow-left' onClick={() => counter > 0 ? setCounter((prevCounter) => prevCounter - 1) : setCounter(list_images.length - 1)} style={{position:'absolute', right:'70%', height:'10vh', width:'auto'}}/>
          <img src={require(`${list_images[counter]}`)} alt='displayed-img' style={{width:'50vw', height:'50vh', border:'1px solid black'}}/>
          <ul style={{position:'absolute', bottom:'5%'}}>
          {list_images.map((element,index) => (
            <>
            <li style={{display:'inline'}}>
            {counter === index ?
              <img src={circle} alt='circle' id={index} style={{height:'3vh', width:'auto'}}/>
              :
              <img src={circle_full} alt='circle_full' id={index} style={{height:'3vh', width:'auto'}} onClick={() => setCounter(index)}/>
            }
            </li>
            </>
          ))
          }
          </ul>
        <img src={arrowRight} alt='arrow-right' onClick={() => counter < list_images.length - 1 ? setCounter((prevCounter) => prevCounter + 1) : setCounter(0)} style={{position:'absolute', left:'70%', height:'10vh', width:'auto'}}/>
    </div>
    <div id='Checkbox'>
      <h3>Are you a Citizen ?</h3>
      {checkOne ?
      <h3>Yes</h3>
      : <h3>No</h3>}
      <h3>Are you over 21 ?</h3>
      {checkTwo ?
      <h3>Yes</h3>
      : <h3>No</h3>}
      <label htmlFor='citizen'>Are you a Citizen ?</label>
      <input type='checkbox' name='citizen' value={checkOne} onChange={() => setCheckOne(!checkOne)}/>
      <label htmlFor='age'>Are you over 21 ?</label>
      <input type='checkbox' name='age' value={checkTwo} onChange={() => setCheckTwo(!checkTwo)}/>
    </div>
    <div id='Login'>
      {loggedIn ? <>Welcome {username}</> :
      <>
      <h2>Login</h2>
      <form onSubmit={(e) => {e.preventDefault() ; handleSubmit()}} >
        <label htmlFor='username'>Username: </label>
        <input type='text' value={username} name='username' onChange={(event) => setUsername(event.target.value)} placeholder='Enter Username' />
        <label htmlFor='password'>Password: </label>
        <input type='password' name='password' value={password} onChange={(event)=>setPassword(event.target.value)} placeholder='Enter Password' />
        <input type='submit' value={'Login'}/>
      </form>
      </>
    }
    </div>
    </>
  );
}

export default App;
