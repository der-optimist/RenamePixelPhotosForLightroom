# RenamePixelPhotosForLightroom

When downloading photos from Google Photos, at least for the ones taken with a Google Pixel the filenames are like

PXL_timestamp.RAW-01.jpg

PXL_timestamp.RAW-02.dng

But Lightroom only recognizes them as "one" phone if everything before the file extension is identical. So this script asks you for a directory and then it renames all files starting with PXL_ so that jpg and dng have identical basenames.



You can download jpg + dng in a bulk via

[https://photos.google.com/search/__tra__](https://photos.google.com/search/_tra_)
