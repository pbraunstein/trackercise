/**
 * Data that wants to be represented in the BarCharts.ts bar chart must implement this interface
 */
export interface BarChartsBar {
    getWidth(): number;
    setWidth(value: number): void;
    getHeight(): number;
    setHeight(): void;
    getWidthBuffer(): number;
    getSets(): number;
}
