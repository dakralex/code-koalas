import {useState} from 'react';
import ReactSlider from 'react-slider'; // Corrected import
import './assets/slider.css';

const Slider = ({min, max, step}: { min: number; max: number; step: number }) => {
    const [currentValue, setCurrentValue] = useState(min);

    return (
        <ReactSlider
            className="customSlider"
            thumbClassName="customSlider-thumb"
            trackClassName="customSlider-track"
            markClassName="customSlider-mark"
            marks={3}
            min={min}
            max={max}
            step={step}
            defaultValue={0}
            value={currentValue}
            onChange={(value) => setCurrentValue(value)}

            /*renderMark={(props) => {
               if (props.key < currentValue) {
                 props.className = "customSlider-mark customSlider-mark-before";
               } else if (props.key === currentValue) {
                 props.className = "customSlider-mark customSlider-mark-active";
               }
               return <span {...props} />;
            }}*/
        />
    );
};

export default Slider;

