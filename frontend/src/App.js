import './App.css';
import DragDropFile from './components/DragDropFile';

function App() {
  return (
    <div className="App">
      <div className="header">
        <h1>DeepTective</h1>
      </div>
      <div className="DragDropFile">
        <DragDropFile />
      </div>
      <div className="footer">
        <p>	&#169; Haris Nazir 2023</p>
      </div>
    </div>
  );
}

export default App;
