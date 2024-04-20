import './assets/app.css'
<<<<<<< HEAD
import Slider from './slider.tsx'

const App = () => (
    <>
        <div className="sidebar"></div>
        <div className="map-container"></div>
        <div className="logo"></div>
        <div className="timeline">
          <Slider min={0} max={48} step={1} />
=======
import 'leaflet/dist/leaflet.css'
import {MapContainer, Polyline} from "react-leaflet";
import coords, {maxLat, maxLongs, minLat, minLongs} from "./globals/outline.ts";
import {LatLng, LatLngBounds} from "leaflet";

const App = () => {
    const outlineCoords = coords.map(p => new LatLng(p[1], p[0]));
    const mapBounds = new LatLngBounds(new LatLng(minLat, minLongs), new LatLng(maxLat, maxLongs));
    const centerCoords = new LatLng((minLat + maxLat) / 2, (minLongs + maxLongs) / 2);

    return <>
        <div className="sidebar">
        </div>
        <div className="map-container">
            <MapContainer bounds={mapBounds} center={centerCoords} minZoom={11} zoom={11} zoomSnap={0.25}
                          style={{width: '100%', backgroundColor: '#242424'}}>
                <Polyline positions={outlineCoords} pathOptions={{color: '#dedede', fillColor: 'none'}}></Polyline>
                
            </MapContainer>
>>>>>>> d60b40aa6aa21df0de38829ed0a903243a17a191
        </div>
    </>
};

export default App
