import './assets/app.css';
import 'leaflet/dist/leaflet.css';
import BASE_LAYER from '../data/processed/baseLayer.json';

import {LatLng, LatLngBounds} from "leaflet";
import {MapContainer, Polyline} from "react-leaflet";
import coords, {maxLat, maxLongs, minLat, minLongs} from "./globals/outline.ts";
import {useEffect, useState} from "react";

const App = () => {
    const outlineCoords = coords.map(p => new LatLng(p[1], p[0]));
    const mapBounds = new LatLngBounds(new LatLng(minLat, minLongs), new LatLng(maxLat, maxLongs));
    const centerCoords = new LatLng((minLat + maxLat) / 2, (minLongs + maxLongs) / 2);

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
                    {...lanes}
                </MapContainer>
            </div>
        </>
    );
};

export default App;

