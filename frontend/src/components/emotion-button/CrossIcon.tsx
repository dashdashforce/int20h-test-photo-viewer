import * as React from 'react';

export interface CrossIconProps {}

const CrossIcon: React.SFC<CrossIconProps> = () => {
  return (
    <svg viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M11.707 10.293a1 1 0 1 0-1.414 1.414l1.414-1.414zm13.586 16.414a1 1 0 0 0 1.414-1.414l-1.414 1.414zm1.414-15a1 1 0 0 0-1.414-1.414l1.414 1.414zM10.293 25.293a1 1 0 0 0 1.414 1.414l-1.414-1.414zm15-15l-15 15 1.414 1.414 15-15-1.414-1.414zm-15 1.414l15 15 1.414-1.414-15-15-1.414 1.414z"
        fill="#000"
      />
    </svg>
  );
};

export default CrossIcon;
