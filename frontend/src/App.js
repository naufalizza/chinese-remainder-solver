import React, { useState, useEffect } from 'react';
import MainForm from './components/MainForm'
import banner from './banner.png';
import './App.css';

function App() {
    return (
        <div className='App'>
            <header className='App-header'>
                <img src={banner} className='App-logo' alt='logo' />
                <MainForm/>
            </header>
        </div>
    );
}
  
  
  // import './App.css';
  
  // function App() {
  //   return (
  //     <div className="App">
  //       {/* <MainForm/>       */}
  //     </div>
  //   );
  // }
export default App;
