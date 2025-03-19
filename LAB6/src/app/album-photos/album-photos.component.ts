import { CommonModule, NgFor } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Photo } from '../models';
import { AlbumsService } from '../albums.service';
import { ActivatedRoute, RouterModule } from '@angular/router';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule, NgFor, RouterModule],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css'
})
export class AlbumPhotosComponent implements OnInit{
  photos: Photo[] =[];

  constructor(private albumService: AlbumsService, private route: ActivatedRoute){

  }

  ngOnInit(): void {
    this.getPhoto();
  }

  getPhoto(){
    this.route.paramMap.subscribe((params) => {
      const albumId: number = Number(params.get('id'));
      console.log("Album ID:", albumId); 
      this.albumService.getPhoto(albumId).subscribe((photos) => {
        console.log("Photos:", photos); 
        this.photos = photos;
      })
    })
  }
  
}