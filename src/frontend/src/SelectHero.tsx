import React, { useState } from 'react';

interface SelectFieldProps {
	options: string[];
	label?: string;
	value?: string;
	onChange?: (selectedValue: string) => void;
}

const SelectField: React.FC<SelectFieldProps> = ({ options, label, value, onChange }) => {
	const [ selectedValue, setSelectedValue ] = useState(value || options[0]);

	const handleValueChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
		const newValue = event.target.value;
		setSelectedValue(newValue);
		if (onChange) {
			onChange(newValue);
		}
	};

	return (
		<div>
			<select value={selectedValue} onChange={handleValueChange}>
				{options.map((option, index) => (
					<option key={index} value={option}>
						{option}
					</option>
				))}
			</select>
		</div>
	);
};

export default SelectField;
