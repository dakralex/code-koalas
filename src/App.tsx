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
    const latLng = L.latLng(lat, long);
    const container = context.map;
    let marker: any;

    // Add a delay of 500 milliseconds before adding the marker
    const addMarkerWithDelay = async () => {
      await timeout(1000);
      marker = L.marker(latLng, {
        icon: L.divIcon({ className: 'custom-marker-icon', iconSize: [2, 2] }) // Adjust the iconSize as needed
      });
      marker.addTo(container);
    };

    addMarkerWithDelay();

    return () => {
      // Ensure that the marker is removed when the component unmounts
      if (marker) {
        container.removeLayer(marker);
      }
    };
  }, [context.map, lat, long]);

  return null;
}


// Function to create a delay
function timeout(delay: number) {
  return new Promise(res => setTimeout(res, delay));
}
//const COORDS = [...Array(15000)].map((_, i) => <Polyline key={i} positions={[[minLat , minLongs], [maxLat, maxLongs]]}/>);

const App = () => {
    const outlineCoords = coords.map(p => new LatLng(p[1], p[0]));
    const mapBounds = new LatLngBounds(new LatLng(minLat, minLongs), new LatLng(maxLat, maxLongs));
    const centerCoords = new LatLng((minLat + maxLat) / 2, (minLongs + maxLongs) / 2);
    const [accidentCoords, setAccidentCoords] = useState<LatLng[]>([]);




useEffect(() => {
  let i = 0;

  const fetchDataAndPlot = () => {
    const month = (i % 12) + 1;
    const year = Math.floor(i / 12) + 2018;

    const filteredAccidents = accidents.filter((accident: any) => accident.year === year && accident.month === month);
    const coords = filteredAccidents.map((accident: any) => new LatLng(accident.lat, accident.lng));

    setAccidentCoords(coords);

    i = (i + 1) % 48;
  };

  const removePoints = () => {
    setAccidentCoords([]);
  };

  const intervalId = setInterval(() => {
    fetchDataAndPlot();
    setTimeout(removePoints, 1000); // Remove points after one second
  }, 2000); // Adjust interval to 2 seconds to account for 1 second delay

  // Clean up the interval when the component unmounts
  return () => clearInterval(intervalId);
}, []);



    return (
        <>
            <div className="sidebar">
            </div>
            <div className="map-container">
                <MapContainer bounds={mapBounds} center={centerCoords} zoom={11} zoomSnap={0.25}
                              style={{width: '100%', backgroundColor: '#242424'}}>
                    <Polyline positions={outlineCoords} pathOptions={{color: '#dedede', fillColor: 'none'}}></Polyline>
                    {accidentCoords.map((coord, index) => (
                      <Point key={index} lat={coord.lat} long={coord.lng} />
                    ))}
                </MapContainer>
            </div>
        </>
    );
};

export default App;

