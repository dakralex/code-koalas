import './assets/app.css'; // Separate import statement for CSS file
import 'leaflet/dist/leaflet.css';
import {MapContainer, Polyline} from "react-leaflet";
import {useLeafletContext} from '@react-leaflet/core';
import coords, {maxLat, maxLongs, minLat, minLongs} from "./globals/outline.ts";
import {LatLng, LatLngBounds} from "leaflet";
import L from 'leaflet';
import {useEffect, useState} from 'react';
import accidents from '../data/processed/accidents.json';


function Point({ long, lat }: { long: number, lat: number }) {
  const context = useLeafletContext();

  useEffect(() => {
    const latLng = L.latLng(lat, long); // Note the order of arguments
    const container = context.map;
    const marker = L.marker(latLng); // Create a marker using the LatLng object
    marker.addTo(container);

    return () => {
      marker.remove(); // Remove the marker when component unmounts
    };
  }, [context.layerContainer, context.map, lat, long]);

  return null;
}
//const COORDS = [...Array(15000)].map((_, i) => <Polyline key={i} positions={[[minLat , minLongs], [maxLat, maxLongs]]}/>);

const App = () => {
    const outlineCoords = coords.map(p => new LatLng(p[1], p[0]));
    const mapBounds = new LatLngBounds(new LatLng(minLat, minLongs), new LatLng(maxLat, maxLongs));
    const centerCoords = new LatLng((minLat + maxLat) / 2, (minLongs + maxLongs) / 2);
    const [accidentCoords, setAccidentCoords] = useState<LatLng[]>([]);

    useEffect(() => {
      console.log('Accidents:', accidents); // Check if accidents data is being loaded correctly
      const coords = accidents.map((accident: any) => new LatLng(accident.lat, accident.lng));
      console.log('Parsed Coordinates:', coords); // Check the parsed coordinates
      setAccidentCoords(coords);
    }, []);

    return (
        <>
            <div className="sidebar">
            </div>
            <div className="map-container">
                <MapContainer bounds={mapBounds} center={centerCoords} zoom={11} zoomSnap={0.25}
                              style={{width: '100%', backgroundColor: '#242424'}}>
                    <Polyline positions={outlineCoords} pathOptions={{color: '#dedede', fillColor: 'none'}}></Polyline>
                   <Point lat={(minLat + maxLat) / 2} long={(minLongs + maxLongs) / 2}></Point>
                    {accidentCoords.map((coord, index) => (
                      <Point key={index} lat={coord.lat} long = {coord.lng} />
                    ))}
                </MapContainer>
            </div>
        </>
    );
};

export default App;

