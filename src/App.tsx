import './assets/app.css';
import 'leaflet/dist/leaflet.css';
import accidents from '../data/processed/accidents.json';
import BASE_LAYER from '../data/processed/baseLayer.json';

import {useEffect, useState} from "react";
import L, {LatLng, LatLngBounds} from "leaflet";
import {MapContainer, Polyline} from "react-leaflet";
import {useLeafletContext} from '@react-leaflet/core';
import coords, {maxLat, maxLongs, minLat, minLongs} from "./globals/outline.ts";


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
      console.log('Accidents:', accidents); // Check if accidents data is being loaded correctly
      const coords = accidents.map((accident: any) => new LatLng(accident.lat, accident.lng));
      console.log('Parsed Coordinates:', coords); // Check the parsed coordinates
      setAccidentCoords(coords);
    }, []);

    const [lanes, setLanes] = useState([]);

    useEffect(() => {
        // @ts-ignore
        const arr = Array.from(BASE_LAYER).map(item => {
            // @ts-ignore
            const latLngPts = item?.coos.map(pt => new LatLng(pt[1], pt[0]));

            return <Polyline positions={latLngPts} />;
        });

        // @ts-ignore
        setLanes(arr)
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
                    {...lanes}
                </MapContainer>
            </div>
        </>
    );
};

export default App;

