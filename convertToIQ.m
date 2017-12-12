function iq=convertToIQ(fileNameRead, fileNameWrite)
fRead=fopen(fileNameRead, 'rb');
iq=fread(fRead,'uint8=>single');
iq=iq-127;
iq=iq/127.0;


fWrite=fopen(fileNameWrite,'wb');
fwrite(fWrite,iq,'single');

fclose(fRead);
fclose(fWrite);
