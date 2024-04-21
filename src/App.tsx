import './assets/app.css';
import 'leaflet/dist/leaflet.css';
import accidents from '../data/processed/accidents.json';
import baseBikeLanes from '../data/processed/baseLayer.json';

import {useEffect, useState} from "react";
import {LatLng, LatLngBounds} from "leaflet";
import {useLeafletContext} from "@react-leaflet/core";
import {MapContainer, Polyline} from "react-leaflet";
import coords, {maxLat, maxLongs, minLat, minLongs} from "./globals/outline.ts";
import "./lib/GLMarkers.js";
// @ts-ignore
import vertex from './assets/shaders/accidents.vert';
// @ts-ignore
import frag from './assets/shaders/accidents.frag';

// @ts-ignore
const BikeLaneLayer = (props) => {
    const context = useLeafletContext();

    // @ts-ignore
    useEffect(() => {
        // @ts-ignore
        const glmarkers = new L.GLMarkerGroup({
            attributes: ['severity'],
            vertexShader: vertex,
            fragmentShader: frag,
        }).addTo(context.map);

        // @ts-ignore
        const coords = Array.from(accidents).forEach(accident => {
            // @ts-ignore
            glmarkers.addMarker(new L.GLMarker(
                [accident.lat, accident.lng],
                {severity: accident.sev}
            ));
        });
    }, []);

    return <>
    </>
};

const App = () => {

    const outlineCoords = coords.map(p => new LatLng(p[1], p[0]));
    const mapBounds = new LatLngBounds(new LatLng(minLat, minLongs), new LatLng(maxLat, maxLongs));
    const centerCoords = new LatLng((minLat + maxLat) / 2, (minLongs + maxLongs) / 2);
    const [laneItems, setLaneItems] = useState([]);

    useEffect(() => {
        // @ts-ignore
        const items = Array.from(baseBikeLanes).map(item => {
            // @ts-ignore
            const latLngPts = item?.coos.map(pt => new LatLng(pt[1], pt[0]));
            return <Polyline positions={latLngPts} pathOptions={{color: '#dedede', fillColor: 'none', weight: 0.875}}/>;
        });

        // @ts-ignore
        setLaneItems(items)
    }, []);

    return (
        <>
            <MapContainer bounds={mapBounds} center={centerCoords} zoom={11} zoomSnap={0.25}
                          style={{width: '100%', backgroundColor: '#242424'}} preferCanvas={true}>
                <Polyline positions={outlineCoords} pathOptions={{color: '#9e9e9e', fillColor: 'none'}} />
                <BikeLaneLayer />
                {...laneItems}
            </MapContainer>
        </>
    );
};

export default App;

