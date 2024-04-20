import './assets/app.css'
import Slider from './slider.tsx'

const App = () => (
    <>
        <div className="sidebar"></div>
        <div className="map-container"></div>
        <div className="logo"></div>
        <div className="timeline">
          <Slider min={0} max={48} step={1} />
        </div>
    </>
);

export default App
