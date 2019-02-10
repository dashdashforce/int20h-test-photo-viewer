import * as React from 'react';

export interface BackIconProps {}

const BackIcon: React.SFC<BackIconProps> = () => {
  return (
    <svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M35 19a1 1 0 1 0 0-2v2zM.293 17.293a1 1 0 0 0 0 1.414l6.364 6.364a1 1 0 0 0 1.414-1.414L2.414 18l5.657-5.657a1 1 0 1 0-1.414-1.414L.293 17.293zM35 17H1v2h34v-2z"
        fill="#000"
      />
    </svg>
  );
};

export default BackIcon;
