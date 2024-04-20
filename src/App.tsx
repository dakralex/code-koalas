import './assets/app.css'; // Separate import statement for CSS file
import 'leaflet/dist/leaflet.css';
import {MapContainer, Polyline} from "react-leaflet";
import coords, {maxLat, maxLongs, minLat, minLongs} from "./globals/outline.ts";
import {LatLng, LatLngBounds} from "leaflet";

//const COORDS = [...Array(15000)].map((_, i) => <Polyline key={i} positions={[[minLat , minLongs], [maxLat, maxLongs]]}/>);

const App = () => {
    const outlineCoords = coords.map(p => new LatLng(p[1], p[0]));
    const mapBounds = new LatLngBounds(new LatLng(minLat, minLongs), new LatLng(maxLat, maxLongs));
    const centerCoords = new LatLng((minLat + maxLat) / 2, (minLongs + maxLongs) / 2);

    return (
        <>
            <div className="sidebar">
            </div>
            <div className="map-container">
                <MapContainer bounds={mapBounds} center={centerCoords} zoom={11} zoomSnap={0.25}
                              style={{width: '100%', backgroundColor: '#242424'}}>
                    <Polyline positions={outlineCoords} pathOptions={{color: '#dedede', fillColor: 'none'}}></Polyline>
                </MapContainer>
            </div>
        </>
    );
};

export default App;

